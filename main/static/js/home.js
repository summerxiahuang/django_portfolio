document.addEventListener('DOMContentLoaded', function() {
    const nameSearch = document.getElementById('name-search');
    const tags = document.querySelectorAll('.tag');
    const projects = document.querySelectorAll('.project-card');


    function filterProjects() {
        const nameQuery = nameSearch.value.toLowerCase();
        projects.forEach((project) => {
            const name = project.querySelector('h3').textContent.toLowerCase();
            const nameMatch = name.includes(nameQuery);
            if (nameMatch) {
                project.style.display = 'block';
            } else {
                project.style.display = 'none';
            }
        });
    }

    tags.forEach((tag) => {
        tag.addEventListener('click', function() {
            const tagName = this.getAttribute('data-tag').toLowerCase();
            projects.forEach((project) => {
                const dataTags = project.getAttribute('data-tags');
                if (!dataTags) {
                    project.style.display = 'none';
                    return;
                }
                const projectTags = dataTags.toLowerCase().split(',').map(t => t.trim());
                const tagMatch = projectTags.includes(tagName);
                if (tagMatch) {
                    project.style.display = 'block';
                } else {
                    project.style.display = 'none';
                }
            });
        });
    });

    nameSearch.addEventListener('input', filterProjects);
});
