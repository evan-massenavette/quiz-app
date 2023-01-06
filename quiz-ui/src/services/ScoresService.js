import StorageService from "@/services/StorageService";

/**
 * Add ranks to all of participations, starting from bestRank.
 * Assumes the array is sorted from best to workst rank
 * @param {{playerName: String, score: Number}[]} registeredScores
 * @param {Number} bestRank The highest
 **/
function addRanks(registeredScores, bestRank = 1) {
  sort(registeredScores)

  // Add rank to each participation
  registeredScores.forEach((element, index) => element.rank = bestRank + index);
}

/**
 * Sort the array of participation (best score will be first)
 * @param {{playerName: String, score: Number}[]} registeredScores 
 */
function sort(registeredScores) {
  registeredScores.sort((a, b) => b.score - a.score);
}

/**
 * Keep only the highest scores 
 * @param {{playerName: String, score: Number, rank: Number}[]} registeredScores 
 */
function getHighestScores(registeredScores) {
  return registeredScores.slice(0, 10);
}

/**
 * @param {{playerName: String, score: Number, rank: Number}[]} registeredScores 
 * @returns {{playerName: String, score: Number, rank: Number}[]} The scores near the current participation
 */
function getScoresNearYou(registeredScores) {
  const yourHighestScore = getYourHighestScore(registeredScores);

  // Find index of current user participation
  const playerName = StorageService.getPlayerName();
  const yourIndex = registeredScores.findIndex(p => p.playerName === playerName && p.score == yourHighestScore);

  // return registeredScores.slice(yourIndex - 5, yourIndex + 5);
  const range = 2
  return registeredScores.slice(
    Math.max(0, yourIndex - range),
    Math.min(registeredScores.length, yourIndex + range)
  );
}

/**
 * @returns {Number} The score of the current participation
 */
function getYourScore() {
  return StorageService.getParticipationScore();
}

/**
 * @param {{playerName: String, score: Number, rank: Number}[]} registeredScores 
 * @returns {Number} The highest score of the currently logged in user
 */
function getYourHighestScore(registeredScores) {
  const playerName = StorageService.getPlayerName();
  return registeredScores
    .filter(p => p.playerName == playerName)
    .map(p => p.score)
    .reduce((a, b) => Math.max(a, b), -Infinity);
}

/**
 * @param {{playerName: String, score: Number, rank: Number}[]} registeredScores 
 * @returns {Number} The highest score of the currently logged in user
 */
function getYourRank(registeredScores) {
  const playerName = StorageService.getPlayerName();
  const yourHighestScore = getYourHighestScore(registeredScores);
  return registeredScores
    .find(p => p.playerName === playerName && p.score === yourHighestScore)
    .rank;

}

export default {
  getYourScore,
  getYourHighestScore,
  addRanks,
  getScoresNearYou,
  getHighestScores,
  sort,
  getYourRank,
}