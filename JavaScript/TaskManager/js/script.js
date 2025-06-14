// hmtl Elements
const taskInput = document.getElementById('task-input');
const addTaskBtn = document.getElementById('add-task-btn');
const taskList = document.getElementById('task-list');

let tasks = []

// Add task function
function addTask(task) {
    tasks.push({text: task, completed: false});
    renderTask();
}

function renderTask() {
    taskList.innerHTML = '';
    tasks.forEach((task, index) => {
        // Creating the element in html file
        const taskElement = document.createElement('li');

        // Adding element to class named 'task'
        taskElement.classList.add('task');

        // If the task has been completed we add element to class named 'completed'
        if (task.completed) {
            taskElement.classList.add('completed');
        }

        // Updating the html file
        taskElement.innerHTML = `
        ${task.text}
        <button class='completed-btn'>Complete</button>
        <button class='delete-btn'>Delete</button>
        `;
        taskElement.querySelector('.completed-btn').addEventListener('click', () => {
            task.completed = !task.completed;
            renderTask();
        });
        taskElement.querySelector('.delete-btn').addEventListener('click', () => {
            tasks.splice(index, 1);
            renderTask();
        });
        taskList.appendChild(taskElement);
    });
}

// Event listener
addTaskBtn.addEventListener('click', () => {
    const task = taskInput.value.trim();
    if (task) {
        addTask(task)
        taskInput.value = '';
    }
});