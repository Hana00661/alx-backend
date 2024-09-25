import Redis from 'redis';

const client = Redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (error) => console.log(`Redis client not connected to the server: ${error.message}`));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.log(error);
    } else {
      console.log(reply);
    }
  });
}

function displaySchoolValue(schoolName) {
  console.log(client.get(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
