class TopNav{

    readTabs(tabs){
        let tab;
        for (let i = 0; i < tabs.length; i ++){
            tab = tabs[i];
            let name = tab.Name;
            topnav.addLinks(name);
        };
    }

    addLinks(name) {
        const links = [
            { text: name, href: '#link1' }
        ];

        // Loop through the links and create a new list item for each
        links.forEach(link => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.textContent = link.text;
            a.href = link.href;
            a.onclick = function(event) {
                event.preventDefault();
            };
            li.appendChild(a);
            const linkList = document.getElementById('link-list');
            linkList.appendChild(li);
        });
    }

    
}