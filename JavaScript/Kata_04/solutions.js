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

/**
 * @param {Map} students
 * @param {String} studentId
 * @returns {Number}
 */
function calculateAverage(students, studentId) {
    return students[studentId].reduce((a,b) => a+b, 0) / students[studentId].length;
}

