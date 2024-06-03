async function lockedProfile() {
    const baseURL = 'http://localhost:3030/jsonstore/advanced/profiles'

    let Response = await fetch(baseURL)
    let profilesData = await Response.json()

    let mainElement = document.getElementById('main')
    mainElement.innerHTML = ''

    let profileCounter = 1
    for (let [ID, profileInfo] of Object.entries(profilesData)) {
        let divProfile = document.createElement('div')
        divProfile.className = 'profile'

        let profileHTML = `
            <img src="./iconProfile2.png" class="userIcon" />
            <label>Lock</label>
            <input type="radio" name="user${profileCounter}Locked" value="lock" checked>
            <label>Unlock</label>
            <input type="radio" name="user${profileCounter}Locked" value="unlock"><br>
            <hr>
            <label>Username</label>
            <input type="text" name="user${profileCounter}Username" value="${profileInfo.username}" disabled readonly />
            <div class="user${profileCounter}HiddenFields">
                <hr>
                <label>Email:</label>
                <input type="email" name="user${profileCounter}Email" value="${profileInfo.email}" disabled readonly />
                <label>Age:</label>
                <input type="email" name="user${profileCounter}Age" value="${profileInfo.age}" disabled readonly />
            </div>
            
            <button>Show more</button>
        `

        divProfile.innerHTML = profileHTML
        divProfile.querySelector('div').style.display = 'none'
        mainElement.appendChild(divProfile)

        let showMoreButton = divProfile.querySelector('button')
        showMoreButton.addEventListener('click', moreInfo)

        function moreInfo() {
            let lockRadioButton = divProfile.querySelector('input[type="radio"]')
            
            if (showMoreButton.textContent === 'Show more' && !lockRadioButton.checked) {
                divProfile.querySelector('div').style.display = 'block'
                showMoreButton.textContent = 'Hide it'
            } else if (showMoreButton.textContent === 'Hide it' && !lockRadioButton.checked) {
                divProfile.querySelector('div').style.display = 'none'
                showMoreButton.textContent = 'Show more'
            }
        }

        profileCounter += 1
    }
}