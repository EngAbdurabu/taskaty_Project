import argparse  # هي الوحدة التي تجعل التطبيق يعمل على سطر الاوامر
from argparse import (
    ArgumentParser,
)  # هذا الصنف يحول ما يدخله المستخدم الى كائن تقدر تتعامل معه للغة بايثون
from taskaty.TaskController import TaskController


def main():
    controller = TaskController("tasks.txt")

    parser = ArgumentParser(
        description="Simple CLI task manger",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # يقوم بعملية التحليل للمدخلات من المستخدم
    # use decrcription to descripe the project
    #  و الا  المحلل لن يتعرف عليهاparse_args()  يجب استدعى كل الوسائط قبل استداع
    # parser.add_argument('add') # to add some thing
    parser.set_defaults(func=None)
    subparser = parser.add_subparsers()

    # add tas
    add_task = subparser.add_parser("add", help="Add the given task: ")
    add_task.add_argument("title", help="Title of the task", type=str)
    add_task.add_argument(
        "-d",
        "--description",
        help="Short description of the task",
        type=str,
        default=None,
    )  # use default use to set value if the user note enter
    add_task.add_argument(
        "-s", "--start_date", help="Date to begin the task", type=str, default=None
    )
    add_task.add_argument(
        "-e", "--end_date", help="Date to end the task", type=str, default=None
    )
    add_task.add_argument(
        "--done", help="Check whether the task is done or not", default=False
    )
    add_task.set_defaults(func=controller.add_task)

    # list task
    list_tasks = subparser.add_parser("list", help=" List unfinished tasks")
    list_tasks.add_argument(
        "-a", "--all", help="List all the tasks", action="store_true"
    )
    # use action to know what action will done
    list_tasks.set_defaults(func=controller.tabulate)

    # check task
    do_task = subparser.add_parser("check", help="Check the given task")
    do_task.add_argument(
        "-t",
        "--task",
        help="Number of the task to be done. If not specified, last task will be removed.",
        type=int,
    )
    do_task.set_defaults(func=controller.do_task)

    # remove task
    remove = subparser.add_parser("remove", help=" Remove a task ")
    remove.add_argument(
        "-t", "--task", help="The task to be removed ( Number )", type=int
    )
    remove.set_defaults(func=controller.remove)

    # reset
    reset = subparser.add_parser("reset", help="Remove all tasks.")
    reset.set_defaults(func=controller.reset)

    args = parser.parse_args()  # يحول التطبيع الى تطبيق في سطر الاورامر
    if not args.func:
        return
    args.func(args)


if __name__ == "__main__":  # لتجنب عمل الشفره عند استدعاها في ملف اخر
    main()
