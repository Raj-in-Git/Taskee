document.addEventListener('DOMContentLoaded', () => {
    console.log("Page loaded!");
    const rows = document.querySelectorAll("table tr");
    rows.forEach((row, index) => {
        if(index > 0) {
            row.addEventListener('click', () => {
                // alert(`You clicked on row ${index}`);
            });
        }
    });
});
