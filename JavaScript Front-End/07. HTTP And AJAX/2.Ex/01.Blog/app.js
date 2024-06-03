function attachEvents() {
    const postsURL = 'http://localhost:3030/jsonstore/blog/posts'
    const commentsURL = 'http://localhost:3030/jsonstore/blog/comments'

    let loadPostsButton = document.getElementById('btnLoadPosts')
    loadPostsButton.addEventListener('click', loadPostsEvent)

    let postsSelect = document.getElementById('posts')

    let viewPostButton = document.getElementById('btnViewPost')
    viewPostButton.addEventListener('click', viewPostEvent)

    allPosts = {}

    async function loadPostsEvent(event) {
        postsSelect.innerHTML = ''
        let allPostsResponse = await fetch(postsURL)
        allPosts = await allPostsResponse.json()
        
        for (let postArr of Object.entries(allPosts)) {
            let option = document.createElement('option')
            option.textContent = postArr[1].title
            option.value = postArr[0]
            postsSelect.appendChild(option)
        }
    }

    async function viewPostEvent(event) {
        let currentPostObject = document.getElementById('posts')
        let currentPostComments = []

        let allCommentsResponse = await fetch(commentsURL)
        let allComments = await allCommentsResponse.json()
        
        for (let commentArr of Object.entries(allComments)) {
            if (commentArr[1].postId === currentPostObject.value) {
                currentPostComments.push(commentArr[1].text)
            }
        }

        let currentPost = allPosts[currentPostObject.value]
    
        let titleElement = document.getElementById('post-title')
        titleElement.textContent = currentPost.title

        let postContentElement = document.getElementById('post-body')
        postContentElement.textContent = currentPost.body

        let commentsUlElement = document.getElementById('post-comments')
        commentsUlElement.innerHTML = ''
        for (let comment of currentPostComments) {
            let commentLiElement = document.createElement('commentLiElement')
            commentLiElement.textContent = comment
            commentsUlElement.appendChild(commentLiElement)
        }
    }
}

attachEvents();