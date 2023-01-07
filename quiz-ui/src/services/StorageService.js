export default {
  // Session storage (front office)
  clear() {
    window.sessionStorage.clear();
  },
  savePlayerName(playerName) {
    window.sessionStorage.setItem("playerName", playerName);
  },
  getPlayerName() {
    return window.sessionStorage.getItem("playerName");
  },
  saveParticipationScore(participationScore) {
    window.sessionStorage.setItem("score", participationScore);
  },
  getParticipationScore() {
    return window.sessionStorage.getItem("score");
  },
  // Local storage (back office)
  saveToken(token) {
    window.localStorage.setItem("token", token);
  },
  getToken() {
    return window.localStorage.getItem("token");
  },
  deleteToken() {
    window.localStorage.removeItem("token");
  },
};
