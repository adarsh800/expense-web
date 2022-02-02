const searchField = document.querySelector('#searchField');
const table_output = document.querySelector('.table-output');
table_output.style.display = 'none';
const appTable = document.querySelector(".app-table");
const paginationContainer = document.querySelector(".pagination-container");
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body");


searchField.addEventListener("keyup", (e)=>{
    const searchVal = e.target.value
    
    // console.log('Search Value:',searchVal)

    if(searchVal.trim().length > 0){
        fetch("/orders/search-order",{
            body: JSON.stringify({searchText : searchVal}),
            method: 'POST',
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('Data:',data);
            tableOutput.style.display = "block";
            console.log("data.length", data.length);
            
            if (data.length === 0) 
            {
          noResults.style.display = "block";
          tableOutput.style.display = "none";
        }
         else {
          noResults.style.display = "none";
          data.forEach((item) => {
            tbody.innerHTML += `
                <tr>
                <td>${item.amount}</td>
                <td>${item.category}</td>
                <td>${item.description}</td>
                <td>${item.date}</td>
                </tr>`;
          });
        }



        });
    }
});
