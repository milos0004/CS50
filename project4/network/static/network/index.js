
document.addEventListener('DOMContentLoaded', function() {
    var imageElements = document.querySelectorAll('.likeimg');
      imageElements.forEach(function(element) {
    // Assign the "like" function as the click event handler
            element.onclick = like;
    });

})
function like(event){
    var imageElement = event.target;
    if(imageElement.src == 'https://i.ibb.co/x8c9xC1/download-removebg-preview-1.png')
    {
        
        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch('/like/'+imageElement.dataset.postid , {
            method: 'POST',
            headers: {'Content-Type': 'application/json','X-CSRFToken': csrftoken},
            body: ''
          })
          .then(response => response.json())
          .then(result => {
              // Print result
              console.log(result);
          })
          .catch(error => {      
            console.log("error", error)
          }
      
          );

        imageElement.src = 'https://i.ibb.co/k90YGq6/download-removebg-preview.png'
        imageElement.parentNode.querySelector("span").innerHTML = parseInt(imageElement.dataset.likecount) - 1
        imageElement.dataset.likecount = parseInt(imageElement.dataset.likecount) - 1

    }
    else
    {
        imageElement.src = 'https://i.ibb.co/x8c9xC1/download-removebg-preview-1.png'
        imageElement.parentNode.querySelector("span").innerHTML = parseInt(imageElement.dataset.likecount) + 1
        imageElement.dataset.likecount = parseInt(imageElement.dataset.likecount) + 1
    }   
}
