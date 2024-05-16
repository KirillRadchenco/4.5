const TelegramBot = требовать ('node-telegram-bot-api');
токен const = 'YOUR_BOT_TOKEN';
const bot = новый TelegramBot(токен, {опрос: true});

// Определяем команды меню
бот.Устанавливает команды ([
 {command: '/start', description: 'Начать работу с ботом'},
 {command: '/help', description: 'Получить справку'},
 {command: '/новаякоманда', description: 'Новая команда'},
]);

// Обработчик новой команды
bot.onText(/\/новаякоманда/, (msg) => {
 постоянный чат = msg.chat.id;
 bot.sendMessage(chatId, 'Вы вызвали новую команду!');
});