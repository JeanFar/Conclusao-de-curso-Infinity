const resources = [];

function addResource(name, type) {
    resources.push({ name, type });
    displayResources();
}

function displayResources() {
    const resourceList = document.getElementById('resourceList');
    resourceList.innerHTML = '';

    resources.forEach(resource => {
        const li = document.createElement('li');
        li.textContent = `${resource.name} - ${resource.type}`;
        resourceList.appendChild(li);
    });
}

document.getElementById('resourceForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('resourceName').value;
    const type = document.getElementById('resourceType').value;

    addResource(name, type);
});
