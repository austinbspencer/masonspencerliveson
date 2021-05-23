module.exports = {
  name: "json-sorter",
  description: "Help sort json array",
  /**
   * This command is a simple call and response
   *
   * @param {prop} string json key to be sorted on
   *
   * @return {number} 1 if greater than -1 if less than or 0 if equal
   */
  json(prop) {
    return function (a, b) {
      if (new Date(a[prop]) < new Date(b[prop])) {
        return 1;
      } else if (new Date(a[prop]) > new Date(b[prop])) {
        return -1;
      }
      return 0;
    };
  },
};
