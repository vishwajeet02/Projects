from Service.task_service import Task_Service
from Service.user_service import User_Service

def main():
    task_service = Task_Service()
    user_service = User_Service()

    user_service.add_user(123,"vishwa","vishwa02@gmail.com")

    task_service.create_task(1,"Teach dsa basic","tech from Scratch")
    task_service.create_task(2,"Teach Advcne dsa","teach from Scratch")
    task_service.create_task(3,"Do a project","teach from Scratch")
    task_service.create_task(4,"Taking order from ak official","fix errors")
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())


    history = task_service.get_task_history()
    print("History")
    print(len(history.pop().title))
    print(len(history.pop().title))
    print(len(history.pop().title))
    print(len(history.pop().title))

if __name__ == '__main__':
    main()