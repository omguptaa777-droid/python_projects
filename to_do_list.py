class To_DO_List:

    def __init__(self):
        self.myList= []
        self.load_list()

    def add_task(self):
        task= input("Add a task:")
        self.myList.append(task)
        self.save_list()
        print("Task added successfully!")
    
    def view_task(self):
        with open("my_tasks.txt","r") as f:
            content= f.read()
            f.close()
        print(content)
    
    def update_task(self):
        self.view_task()
        n= int(input('Enter the index of the task you want to update:'))
        self.myList[n]= input("Update the task with the new task:")
        self.save_list()
        print("New task successfully updated!")
    
    def delete_task(self):
        self.view_task()
        n= int(input('Enter the index of the task you want to delete:'))
        item= self.myList.pop(n)
        self.save_list()
        print("Task deleted successfully!")
        
    
    def save_list(self):
        with open("my_tasks.txt","w") as f:
         for task in self.myList:
          f.write(task + '\n')
         f.close()

    def load_list(self):
        # Load tasks from the file into the list
        try:
            with open("my_tasks.txt", "r") as f:
                self.myList = [line.strip() for line in f]
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty list
            self.myList = []
    
obj= To_DO_List()
print('''
      Enter 1 to add a task
      Enter 2 to view  tasks
      Enter 3 to update a task
      Enter 4 to delete a task
      Enter 5 to save the list
      
      ''')

n= int(input("Enter your choice:"))

if n==1:
    num= int(input("Enter number of tasks you want to add:"))
    for i in range(num):
        obj.add_task()
         
elif n==2:
    obj.view_task()

elif n==3:
    obj.update_task()

elif n==4:
    num= int(input("Enter number of tasks you want to add:"))
    for i in range(num):
     obj.delete_task()

else:
    print("Invalid choice. Please try again.")

obj.save_list()


         