// Funções básicas de interação com o frontend

// Exibe mensagens de sucesso ou erro ao interagir com o backend
function showNotification(message, type) {
    const notification = document.createElement('div');
    notification.textContent = message;
    notification.className = type === 'error' ? 'notification error' : 'notification success';
    document.body.appendChild(notification);

    // Remove a notificação após 3 segundos
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Exemplo de envio de formulário usando fetch
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());
            const response = await fetch('/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                showNotification('God added successfully!', 'success');
                form.reset();
            } else {
                const error = await response.json();
                showNotification(error.error || 'Failed to add God.', 'error');
            }
        });
    }
});

