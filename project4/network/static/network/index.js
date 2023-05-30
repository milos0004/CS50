
document.addEventListener('DOMContentLoaded', function() {
    var imageElements = document.querySelectorAll('.likeimg');
      imageElements.forEach(function(element) {
    // Assign the "like" function as the click event handler
            element.onclick = like;
            
    });
    var editElements = document.querySelectorAll('.edit');
    editElements.forEach(function(element) {
    // Assign the "like" function as the click event handler
            element.onclick = edit;
            
    });

    
})
function like(event){
    var imageElement = event.target;
    if(imageElement.src == 'https://i.ibb.co/k90YGq6/download-removebg-preview.png')
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

        imageElement.src = 'https://i.ibb.co/x8c9xC1/download-removebg-preview-1.png'
        imageElement.parentNode.querySelector("span").innerHTML = parseInt(imageElement.dataset.likecount) + 1
        imageElement.dataset.likecount = parseInt(imageElement.dataset.likecount) + 1

    }
    else
    {
        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch('/like/'+imageElement.dataset.postid, {
            method: 'DELETE',
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ /* Optional request body */ }),
          })
          .then(response => {
            if (response.ok) {
              // Request was successful
              // Handle the response
            } else {
              // Request failed
              throw new Error('Request failed with status: ' + response.status);
            }
          })
          .catch(error => {
            // Handle the error
          });
          
        imageElement.src = 'https://i.ibb.co/k90YGq6/download-removebg-preview.png'
        imageElement.parentNode.querySelector("span").innerHTML = parseInt(imageElement.dataset.likecount) - 1
        imageElement.dataset.likecount = parseInt(imageElement.dataset.likecount) - 1
    }   
}

function edit(event){
    var editElement = event.target;
    editElement.parentNode.parentNode.querySelector('#content').style.display = 'none';

    var newdiv = document.createElement('div');
    var newtxt = document.createElement('textarea');
    var newbtn = document.createElement('button');
    newbtn.innerHTML="Save";
    newtxt.innerHTML = editElement.parentNode.parentNode.querySelector('#content').innerHTML;
    editElement.appendChild(newdiv);
    newdiv.appendChild(newtxt);
    newdiv.appendChild(newbtn);
    newbtn.onclick = function() {
        editElement.parentNode.parentNode.querySelector('#content').style.display = 'block';
        editElement.parentNode.parentNode.querySelector('#content').innerHTML = newtxt.value;
        newdiv.style.display = 'none';



        var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch('/edit/'+editElement.dataset.postid , {
            method: 'PUT',
            headers: {'Content-Type': 'application/json','X-CSRFToken': csrftoken},
            body: JSON.stringify({
                content: newtxt.value,
            })
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
      };
    

    
}
