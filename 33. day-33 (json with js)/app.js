try {
  const data = require("./sample.json");
  // console.log(data)
  console.log(typeof data);
  console.log(data["name"]);

  for (key in data[0]) {
    if (typeof data[key] !== "object") console.log(key, "--", data[0]);
  }
} catch (err) {
  console.log(err);
}
