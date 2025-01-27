//function for deleting notes
function deleteNote(noteId) {
    //go to /delete-note endpoint
    fetch('/delete-note', {
        method: 'POST',
        //turn note into jason string
        body: JSON.stringify({ noteId: noteId})
    }),then((_res) => {
        //redirect to home (essentially refresh the page)
        window.location.href = "/";
    });
}


