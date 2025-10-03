import argparse
from datetime import datetime 
from taskpad_func import add_task, update_task, delete_task, mark_in_progress, mark_done, list_tasks

def main():
    parser = argparse.ArgumentParser(description='Task Tracker', add_help = True) # this is how we use the cli by describing what we will using it for
    subparsers = parser.add_subparsers(dest='command') # this is for the commands for example add or delete something
   
    add_parse = subparsers.add_parser('add', help='Task to be added') # so this will be shown to the user with a little help guide on what the command does
    add_parse.add_argument(
        "description",
        type=str,
        nargs="+",
        help="Description of the task to add"
    ) # here it is a string that will be added and we can have multiple strings for example Get water from Lulu without having to input "Get water from Lulu" so the user can just input their text without quotation marks
    
    update_parse = subparsers.add_parser('update', help='Task ID followed by task description to be update')
    update_parse.add_argument(
        "task_id",
        type=int,
        help='ID of the task to be updated'
    )
    update_parse.add_argument(
        "description",
        type=str,
        nargs="+",
        help='description of the task to be updated'
    )
    
    mark_in_progress_parse = subparsers.add_parser('mark-in-progress', help='Task ID to be marked as in progress')
    mark_in_progress_parse.add_argument(
        "task_id",
        type=int,
        help='ID of the task to be marked as in-progress'
    )
    
    mark_done_parse = subparsers.add_parser('mark-done', help='Task ID to be marked as done')
    mark_done_parse.add_argument(
        "task_id",
        type =int,
        help='ID of the task to be marked as done'
    )
    
    delete_parse = subparsers.add_parser('delete', help='Task ID to be deleted')
    delete_parse.add_argument(
        "task_id",
        type =int,
        help='ID of the task to be deleted'
    )
   
    #with the list we have multiple sub command where we filter the list based on the status, creation or update year/ year-month-date
    list_parse = subparsers.add_parser('list',help='List all the tasks or filter based on status or date')
    list_parse.add_argument(
        "-s","--status",
        help="Filter tasks by status (todo, done, in-progress)",
        type=str,
        choices=["todo","done","in-progress"])
    list_parse.add_argument(
        '-c',"--created",
        help="Filter tasks by creation date (YYYY or YYYY-MM-DD)",
        type=str,
    )
    list_parse.add_argument(
        '-u',"--updated",
        help="Filter tasks by updated date (YYYY or YYYY-MM-DD)",
        type=str,
    )
    
    # this where we call our function so that it runs 
    args = parser.parse_args()
   
    #conditional statement on what actions to perform when each command is given
    if args.command == 'add':
        result = add_task(" ".join(args.description)) # the .join() function here assists with the multiple strings written without quotation marks so that they will be parsed properly
        print(result) # produce a table for each output
    elif args.command == 'update':
        result = update_task(args.task_id," ".join(args.description))
        print(result)
    elif args.command == 'delete':
        result = delete_task(args.task_id)
        print(result)
    elif args.command == 'mark-in-progress':
        result = mark_in_progress(args.task_id)
        print(result)
    elif args.command == 'mark-done':
        result = mark_done(args.task_id)
        print(result)
    elif args.command == 'list':
        result = list_tasks(status=args.status, created=args.created, updated=args.updated)
        print(result)
    else:
        parser.print_help() # if none of this added then we print the help statement so that they know what command to use


if __name__ == "__main__":
    main()
