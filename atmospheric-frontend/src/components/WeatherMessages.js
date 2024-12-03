const messages = {
  clear: {
    day: [
      "The sky is clear. Perfect time for a walk!",
      "It's sunny! Don't forget your sunscreen.",
      "A bright day ahead—embrace the sunshine!",
      "Clear skies are calling for a picnic.",
      "Lovely clear weather! Don't forget sunscreen if you're heading out.",
    ],
    night: [
      "The sky is clear tonight. Perfect for stargazing!",
      "Clear night skies—maybe you'll spot a shooting star!",
      "It's a clear night—enjoy the moonlight.",
      "Lovely clear weather tonight! Have sweet dreams.",
    ],
  },
  rain: {
    day: [
      "It's raining—don’t forget your umbrella!",
      "A perfect day for puddle jumping—waterproof boots are a must!",
      "Raindrops are falling—how about a hot cup of cocoa?",
      "It's rainy, stay dry out there!",
      "Showers ahead—great weather for a cozy movie day.",
      "Stay dry! Perfect weather for a book and hot tea.",
      "Don't let the rain dampen your day; stay cozy inside!",
    ],
    night: [
      "Rainy night—perfect time to listen to the raindrops as you sleep.",
      "It's raining tonight—stay warm and cozy indoors.",
      "Raindrops are falling—have a restful night.",
      "Rainy nights are perfect for reading a book in bed.",
    ],
  },
  snow: {
    day: [
      "It's snowing! A great day to build a snowman.",
      "Bundle up—it's a winter wonderland out there!",
      "Snowflakes are falling—grab your scarf and gloves.",
      "Cold and snowy—perfect for sledding or staying warm inside.",
      "It's snowy! Time to build a snowman or stay warm indoors.",
      "A winter wonderland outside! Drive safely.",
    ],
    night: [
      "Snowy night—enjoy the quiet beauty of snowfall.",
      "It's snowing tonight—perfect for a cozy evening indoors.",
      "A snowy night—stay warm and have sweet dreams.",
    ],
  },
  fog: {
    day: [
      "There's fog—drive safe and stay cautious!",
      "Misty views outside—perfect for a reflective walk.",
      "Foggy mornings call for a warm cup of tea.",
      "Visibility is low—keep your lights on if you're driving.",
      "There's fog; please be safe while traveling!",
      "Low visibility today; take extra care on the roads.",
      "A foggy day! Great time to enjoy the stillness indoors.",
    ],
    night: [
      "Foggy night—be careful if you're out and about!",
      "The fog adds a mysterious touch to the night.",
      "Foggy night skies—stay safe and cozy inside.",
    ],
  },
  wind: {
    day: [
      "It's windy—hold onto your hat!",
      "A blustery day—perfect for flying kites!",
      "Strong winds—secure outdoor items.",
      "The wind is howling—a perfect excuse to stay cozy indoors.",
    ],
    night: [
      "Windy night—listen to the whispers of the wind.",
      "It's windy tonight—stay warm inside!",
      "Blustery winds outside—perfect for a snug evening indoors.",
    ],
  },
  drizzle: {
    day: [
      "A light drizzle—don’t forget a raincoat!",
      "Soft rain—great weather for a reflective stroll.",
      "Drizzly weather—time to unwind with a good book.",
    ],
    night: [
      "A gentle drizzle tonight—sleep tight!",
      "Drizzly night—perfect for a peaceful sleep.",
      "Light rain outside—have a cozy evening indoors.",
    ],
  },
  thunderstorm: {
    day: [
      "Thunderstorms today! Stay safe and unplug devices.",
      "Booming skies! Enjoy the light show from indoors.",
      "Thunderstorms are rolling in; time to stay cozy inside!",
    ],
    night: [
      "Thunderstorms tonight—stay safe and rest well.",
      "Stormy night—perfect for watching the lightning from indoors.",
      "Thunder is rumbling—have a safe and peaceful night.",
    ],
  },
  clouds: {
    day: [
      "It's a bit cloudy, but that just makes the day cozier!",
      "Cloudy skies—perfect weather for a warm cup of coffee.",
      "The clouds are out; maybe the sun is playing hide and seek!",
      "Overcast days are great for relaxing indoors.",
      "Don't let the clouds dull your sparkle today!",
    ],
    night: [
      "Cloudy night—perfect for a cozy evening indoors.",
      "The stars might be hiding, but it's a great night to relax!",
      "Clouds blanket the night sky—sleep tight!",
      "A peaceful cloudy night—sweet dreams await!",
      "Cloudy skies tonight; a perfect time for a good book before bed.",
    ],
  },
  default: {
    day: [
      "Enjoy your day, no matter the weather!",
      "Make the most of today!",
      "A great day to make memories.",
    ],
    night: [
      "Have a peaceful night!",
      "Sweet dreams!",
      "Rest well for tomorrow's adventures.",
    ],
  },
};

export function getSweetMessage(description, isNightTime) {
  const type = description.toLowerCase();
  console.log(`Weather description: ${type}`);
  console.log(`Is it nighttime? ${isNightTime}`);

  // Map common weather descriptions to categories
  const descriptionMap = {
    clear: "clear",
    "clear sky": "clear",
    rain: "rain",
    "light rain": "rain",
    "moderate rain": "rain",
    drizzle: "drizzle",
    snow: "snow",
    thunderstorm: "thunderstorm",
    clouds: "clouds",
    "few clouds": "clouds",
    "scattered clouds": "clouds",
    "broken clouds": "clouds",
    "overcast clouds": "clouds",
    mist: "fog",
    fog: "fog",
    haze: "fog",
    smoke: "fog",
    dust: "fog",
    sand: "fog",
    ash: "fog",
    squall: "wind",
    tornado: "wind",
  };

  let category = null;

  // Find the category based on description
  for (const key in descriptionMap) {
    if (type.includes(key)) {
      category = descriptionMap[key];
      console.log(`Matched description "${key}" to category "${category}"`);
      break;
    }
  }

  if (category && messages[category]) {
    let possibleMessages = isNightTime
      ? messages[category].night
      : messages[category].day;
    if (!possibleMessages || possibleMessages.length === 0) {
      // Fallback to day messages if night messages are not available
      possibleMessages = messages[category].day;
    }
    return possibleMessages[
      Math.floor(Math.random() * possibleMessages.length)
    ];
  }
  // Default message if no category matches
  const defaultMessages = isNightTime ? messages.default.night : messages.default.day;
  return defaultMessages[Math.floor(Math.random() * defaultMessages.length)];
}



  
  