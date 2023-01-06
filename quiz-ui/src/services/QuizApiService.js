import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(`Error on ${method.toUpperCase()} to ${resource}`, error);
      });
  },
  // Front office
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    return this.call("get", `questions?position=${position}`);
  },
  getAllQuestions() {
    return this.call("get", "questions/all")
  },
  postScore(playerName, answers) {
    const body = { playerName, answers }
    return this.call("post", "participations", body)
  },
  // Back office
  login(password) {
    const body = { password }
    return this.call("post", "login", body)
  },
  deleteAllQuestions(token) {
    return this.call("delete", "questions/all", null, token)
  },
  deleteAllParticipations(token) {
    return this.call("delete", "participations/all", null, token)
  },
  deleteQuestion(token, id) {
    return this.call("delete", `questions/${id}`, null, token)
  },
  addQuestion(token, text, title, image, position, possibleAnswers) {
    return this.call("post", "questions", { text, title, image, position, possibleAnswers }, token)
  },
  modifyQuestion(token, id, text, title, image, position, possibleAnswers) {
    return this.call("put", `questions/${id}`, { text, title, image, position, possibleAnswers }, token)
  }
};