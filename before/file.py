def save_to_file(file_name, jobs):
    with open(f'{file_name}.csv', 'w', encoding='utf-8') as file:
        for job in jobs:
            file.write(f"{job['title']}, {job['company']}, {job['region']}, {job['link']}\n")
