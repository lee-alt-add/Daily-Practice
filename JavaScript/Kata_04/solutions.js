/**
 * @param {Map} students
 * @param {String} name
 * @param {String} studentId
 * @param {Array} grade
 * 
 */
function addStudent(students, name, studentId, grade) {
    students[studentId] = new Map([[name, grade]]);
}

