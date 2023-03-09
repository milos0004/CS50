document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  fetch('/emails/' + mailbox)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);
      emails.forEach(e => {

        if (e.recipients.includes(document.querySelector('.form-control').value)){


          const element = document.createElement('div');
          if (e.read == false){
            element.className ="containerread"
          }
          else{
            element.className ="containernotread"
          }
          
          //element.innerHTML = e.sender + " " + e.subject + " " + e.timestamp;

          
          element.addEventListener('click', function() {
              console.log('This element has been clicked!')
              view_email(e.id)
          });
          const row = document.createElement('div');
          row.className="row"
          const col1 = document.createElement('div');
          col1.className="col-3"
          col1.innerHTML = e.sender
          const col2 = document.createElement('div');
          col2.className="col-6"
          col2.innerHTML = e.subject
          const col3 = document.createElement('div');
          col3.className="col-3"
          col3.innerHTML = e.timestamp
          element.appendChild(row);
          row.appendChild(col1);
          row.appendChild(col2);
          row.appendChild(col3);
          document.querySelector('#emails-view').append(element);



        }
        else{
          console.log(document.querySelector('.form-control').value);
          console.log(e.recipient);
        }
      });
      // ... do something else with emails ...
  });
  


}

function view_email(email_id) {
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  fetch('/emails/' + email_id)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
  
      // ... do something else with email ...
  });
}