const Kafka = require('no-kafka');

// Create an instance of the Kafka consumer
let valueSum = 0;
let count = 1;

const consumer = new Kafka.SimpleConsumer({"connectionString":"127.0.0.1:9092"})
const data = function (messageSet) {
    messageSet.forEach(function (m) {
        const value = parseInt(m.message.value.toString('utf8'));
        valueSum = valueSum + value;
        console.log(valueSum / count);
        count = count + 1;
    });
};

// Subscribe to the Kafka topic
return consumer.init().then(function () {
    return consumer.subscribe('kafka-python-topic', data);
});