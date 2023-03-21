function getAmount()
{
    let length = document.getElementsByClassName("articles").length;
    
    let div = document.getElementById("articleAmount");
    let p = document.createElement('p');
    p.className = "bottom-text";
    let content = document.createTextNode(length.toString() + " articles currently loaded.");

    p.appendChild(content);
    div.appendChild(p);
}

$(document).ready(function() {
    $("select[name='sortSelection']").change(function() {
        $.ajax({
            type: "POST",
            url: "/changeSort",
            data: JSON.stringify({name: $(this).val()}),
            dataType: 'json',
            contentType: 'application/json',
            success: function() {
                location.reload();
            }
        });
    });
});
