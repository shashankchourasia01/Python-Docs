import sqlite3

con = sqlite3.connect('Youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL 
     )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
    

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()


def main():
    while True:
        print("\nYoutube Manager App With DB")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video's details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your Choice: ")  

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input('Enter the video name: ')
            time = input('Enter the video time: ')            
            add_video(name, time)

        elif choice == '3':
            video_id = int(input('Enter video ID to update: '))
            name = input('Enter the new video name: ')
            time = input('Enter the new video time: ')            
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = int(input('Enter video ID to delete: '))            
            delete_video(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice")

    con.close()  # Close the connection after the loop ends


if __name__ == "__main__":
    main()
