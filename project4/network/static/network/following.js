
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#following').onclick = follow;

})
function follow(event){
    if(document.querySelector('#following').innerHTML == 'Unfollow')
    {
        document.querySelector('#following').innerHTML = 'Follow User'
        // fetch('/follow/' + user)
        // .then(response => response.json())
        
        // .then(f => {


        // });

    }
    else
    {
        document.querySelector('#following').innerHTML = 'Following'
    }   
}
