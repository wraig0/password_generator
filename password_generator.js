const crypto = require("crypto");

const generateRandomString = (length) => {
  const characters =
    " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
  let randomString = "";

  for (let i = 0; i < length; i++) {
    const randomIndex = crypto.randomInt(0, characters.length);
    randomString += characters[randomIndex];
  }

  return randomString;
};

const randomString = generateRandomString(64);
console.log(randomString);
