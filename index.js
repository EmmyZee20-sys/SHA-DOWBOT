import { Client, GatewayIntentBits, Collection } from "discord.js";
import { config } from "dotenv";
import fs from "fs";
import path from "path";

config();

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

client.commands = new Collection();

// Load commands dynamically
const commandPath = path.join("src", "commands");
fs.readdirSync(commandPath).forEach(file => {
  const command = await import(`./src/commands/${file}`);
  client.commands.set(command.default.name, command.default);
});

client.on("messageCreate", (message) => {
  if (!message.content.startsWith("!")) return;

  const args = message.content.slice(1).split(/ +/);
  const commandName = args.shift().toLowerCase();

  const command = client.commands.get(commandName);
  if (command) command.execute(message, args);
});

client.login(process.env.TOKEN);
