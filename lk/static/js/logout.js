function logout() {
    var res = fetch('/rest-auth/logout/', {
        method: 'post',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    })
}