from src.utils.gantt_utils import load_tasks, group_tasks_by_group, plot_gantt

def main():
    
    file_path = 'data/timeline.csv'
    output_path = None

    tasks = load_tasks(file_path)
    print(tasks)
    grouped_tasks = group_tasks_by_group(tasks)
    
    plot_gantt(grouped_tasks, output_path)

if __name__ == "__main__":
    main()