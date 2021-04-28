const Discord = require("discord.js")
const { play } = require('../../structures/radio')

module.exports={
  name: "radio",
  category: "Radio",
  aliases:["rad"],
  utilisation: '{prefix}radio',
  execute: async(client , message, args)=>{
        const { channel } = message.member.voice;

        if (!channel) return message.reply("You need to join a voice channel first!").catch(console.error);
        //if (client.author.voice && channel !== message.guild.me.voice.channel)
          //return message.reply(`You must be in the same channel as ${message.author.username}`).catch(console.error);

        

        const permissions = channel.permissionsFor(message.client.user);
        if (!permissions.has("CONNECT"))
          return message.reply("Cannot connect to voice channel, missing permissions");
        if (!permissions.has("SPEAK"))
          return message.reply("I cannot speak in this voice channel, make sure I have the proper permissions!");

        const radios = new Discord.MessageEmbed()
        radios.setTitle("Radios available")
        radios.setColor('RANDOM')
        radios.setDescription('```A. Radio Mirchi -Tamil \n B. Radio Mirchi - Hindi \n C.Radio City - Hindi \n D.AIR FM Rainbow 100.5 - Tamil ```')
        radios.setFooter('React with reaction to select the radio')

try{
          var playingMessage = await message.channel.send(radios);
      await playingMessage.react("🇦");
      await playingMessage.react("🇧");
      await playingMessage.react("🇨");
      await playingMessage.react("🇩");
    } catch (error) {
      console.error(error);
    }

    const filter = (reaction, user) => user.id !== message.client.user.id;
    var collector = playingMessage.createReactionCollector(filter, {
      time: 60000
    });

    collector.on("collect", (reaction, user) => {
      const member = message.guild.member(user);

      switch (reaction.emoji.name) {
        case "🇦":
        url="https://mirchitoptucker-lh.akamaihd.net/i/MirchiTopTucker_1_1@66103/master.m3u8"
        let name="Radio Mirchi - Tamil"
        play(message, url , name)

        const mt = new Discord.MessageEmbed()
        mt.setAuthor(name)
        
         playingMessage.reactions.removeAll().catch(console.error);
         playingMessage.delete({ timeout: 1000 }).catch(console.error);
        
          break;

        case "🇧":
         url = "https://streams.radio.co/s8d06d0298/listen"
        name="Radio Mirchi-  Hindi"
        play(message, url , name)
         playingMessage.reactions.removeAll().catch(console.error);
         playingMessage.delete({ timeout: 1000 }).catch(console.error);
        
         
          break;

        case "🇨":
        url= "https://prclive4.listenon.in/Hindi"
        name='Radio City - hindi'
        play(message, url , name)
         playingMessage.reactions.removeAll().catch(console.error);
         playingMessage.delete({ timeout: 1000 }).catch(console.error);
        
         
          break;

        case "🇩":
        url= "https://air.pc.cdn.bitgravity.com/air/live/pbaudio051/playlist.m3u8"
        name='AIR FM Rainbow 100.5 - Tamil'
        play(message, url , name)
         playingMessage.reactions.removeAll().catch(console.error);
         playingMessage.delete({ timeout: 1000 }).catch(console.error);
        
         
          break;

        default:
          reaction.users.remove(user).catch(console.error);
          break;
      }
    });

    collector.on("end", () => {
    });

  }
}
