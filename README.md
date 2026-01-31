# To-Do List Application

A simple and intuitive **to-do list application** built with Python's Tkinter library. Organize your tasks efficiently with an easy-to-use graphical interface.

## Features

✨ **Core Functionality:**
- ➕ **Add Tasks** - Quickly add new tasks to your list
- 🗑️ **Delete Tasks** - Remove individual tasks with a single click
- 🔄 **Clear All** - Clear the entire task list at once
- 💾 **Persistent Storage** - Tasks are automatically saved to `tasks.txt`

## Screenshots

The application features a clean, user-friendly interface with:
- Input field for entering new tasks
- Scrollable task list display
- Three action buttons (Add Task, Delete Task, Clear All)
- Color-coded buttons for intuitive navigation

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd To-do
   ```

## Usage

Run the application:
```bash
python main.py
```

### How to Use:
1. **Add a Task** - Type your task in the input field and click "Add Task"
2. **Delete a Task** - Select a task from the list and click "Delete Task"
3. **Clear All Tasks** - Click "Clear All" to remove all tasks at once
4. Tasks are automatically saved and will persist between sessions

## File Structure

```
To-do/
├── main.py           # Main application file
├── tasks.txt         # Auto-generated file containing saved tasks
└── README.md         # Documentation
```

## Technical Details

- **Framework:** Tkinter (Python GUI toolkit)
- **Window Size:** 350x450 pixels (non-resizable)
- **Data Storage:** Plain text file (`tasks.txt`)

## Future Enhancements

Potential improvements for future versions:
- Task priority levels
- Due date tracking
- Task completion checkmarks
- Dark mode support
- Data export functionality

## License

Free to use and modify for personal or educational purposes.

## Author

Created as a simple project to demonstrate Python GUI development with Tkinter.
