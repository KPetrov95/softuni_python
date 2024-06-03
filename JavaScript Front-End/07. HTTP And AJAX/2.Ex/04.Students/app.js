function attachEvents() {
  const baseURL = 'http://localhost:3030/jsonstore/collections/students';

  const tBodyElement = document.querySelector('tbody');
  const submitButtonElement = document.getElementById('submit');
  submitButtonElement.addEventListener('click', createStudent)

  const inputFNameElement = document.querySelector('input[name=firstName') 
  const inputLNameElement = document.querySelector('input[name=lastName')
  const inputFacNumberElement = document.querySelector('input[name=facultyNumber')
  const inputGradeElement = document.querySelector('input[name=grade')

  async function extractStudents() {
    dataResponse = await fetch(baseURL);
    students = await dataResponse.json();

    for(student of Object.values(students)) {
      tRowElement = document.createElement('tr');
      firstNameTd = document.createElement('td');
      lastNameTd = document.createElement('td');
      facNumberTd = document.createElement('td');
      gradeTd = document.createElement('td');

      firstNameTd.textContent = student.firstName;
      tRowElement.appendChild(firstNameTd);
      lastNameTd.textContent = student.lastName;
      tRowElement.appendChild(lastNameTd);
      facNumberTd.textContent = student.facultyNumber;
      tRowElement.appendChild(facNumberTd);
      gradeTd.textContent = student.grade;
      tRowElement.appendChild(gradeTd);
      tBodyElement.appendChild(tRowElement);
    }
  }

  extractStudents()

  async function createStudent() {
    const newStudent = {
      firstName: inputFNameElement.value,
      lastName: inputLNameElement.value,
      facultyNumber: inputFacNumberElement.value,
      grade: inputGradeElement.value,
    }

    await fetch(baseURL, {
      method: 'POST',
      body: JSON.stringify(newStudent)
    })

    extractStudents()
  }
}

attachEvents();