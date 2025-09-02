document.addEventListener('DOMContentLoaded', () => {
    // Find all 'toggle-done' buttons
    const toggleButtons = document.querySelectorAll('.toggle-done');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            event.preventDefault(); // Prevent the default form submission
            
            const taskId = button.dataset.taskId; // Get the task ID from the button's data attribute
            
            try {
                // Send an asynchronous request to your backend
                const response = await fetch(`/api/tasks/${taskId}/toggle`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                
                if (response.ok) {
                    // If the request was successful, update the UI
                    const taskItem = button.closest('li');
                    if (taskItem) {
                        taskItem.classList.toggle('done');
                    }
                } else {
                    console.error('Failed to toggle task status');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });
});