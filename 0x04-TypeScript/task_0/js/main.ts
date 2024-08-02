interface Student {
  firstName: string;
  lastName: string;
  age: number;
  location: string;
}

const Student1: Student = {
  firstName: "Michaell",
  lastName: "Maina",
  age: 19,
  location: "Mombasa, Kenya",
};

const Student2: Student = {
  firstName: "Derrick",
  lastName: "Muturi",
  age: 20,
  location: "Cape town, South Africa",
};

const studentsList: Array<Student> = [Student1, Student2];
const styleSheet = `
 html {
 margin:0;
 height:100%;
 }
 body {
 box-sizing: border-box;
 display:flex;
 align-items:center;
 justify-content:center;
 margin:10%;
 height:80%;
 }
 table {
  border-collapse:collapse;
 }
  thead {
    font-weight:bold;
  }
  td {
    padding:10px;
    border:1px solid gray;
    cursor:pointer;
  }
  td:hover {
    background: gainsboro;
  }
  td:nth-child(1) {
    text-align:center;
  }
`;

export const displayTable = (students: Array<Student>) => {
  const table = document.createElement("table");
  const tableHead = document.createElement("thead");
  const headRow = document.createElement("tr");
  const tableBody = document.createElement("tbody");

  headRow.insertAdjacentHTML("beforeend", "<td>FirstName</td>");
  headRow.insertAdjacentHTML("beforeend", "<td>Location</td>");
  tableHead.insertAdjacentElement("beforeend", headRow);

  for (const student of students) {
    const bodyRow = document.createElement("tr");
    bodyRow.insertAdjacentHTML("beforeend", `<td>${student.firstName}</td>`);
    bodyRow.insertAdjacentHTML("beforeend", `<td>${student.location}</td>`);
    tableBody.insertAdjacentElement("beforeend", bodyRow);
  }

  table.insertAdjacentElement("beforeend", tableHead);
  table.insertAdjacentElement("beforeend", tableBody);
  document.body.insertAdjacentElement("beforeend", table);
};

displayTable(studentsList);
const styleSheetElement = document.createElement("style");
styleSheetElement.innerHTML = styleSheet;
document.head.insertAdjacentElement("beforeend", styleSheetElement);
document.title = "Task 0";
