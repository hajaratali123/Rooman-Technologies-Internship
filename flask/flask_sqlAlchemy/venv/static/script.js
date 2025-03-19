document.addEventListener("DOMContentLoaded", fetchUsers);

document.getElementById("userForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const response = await fetch("/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email }),
    });

    if (response.ok) {
        fetchUsers();
        document.getElementById("userForm").reset();
    }
});

async function fetchUsers() {
    const response = await fetch("/users");
    const users = await response.json();
    const userList = document.getElementById("userList");
    userList.innerHTML = "";

    users.forEach(user => {
        const li = document.createElement("li");
        li.innerHTML = `${user.name} - ${user.email} 
            <button class="delete" onclick="deleteUser(${user.id})">Delete</button>`;
        userList.appendChild(li);
    });
}

async function deleteUser(id) {
    const response = await fetch(`/users/${id}`, { method: "DELETE" });
    if (response.ok) {
        fetchUsers();
    }
}
