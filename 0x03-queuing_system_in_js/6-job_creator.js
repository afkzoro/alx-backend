const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a test message.',
};

const job = queue.create('push_notification_code', jobData)
  .save((error) => {
    if (!error) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log('Notification job failed');
    }
    queue.shutdown(5000, () => {
      process.exit(0);
    });
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
