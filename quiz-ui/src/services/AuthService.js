import * as jose from 'jose'
import QuizApiService from '@/services/QuizApiService'
import StorageService from '@/services/StorageService'

let _isAuthenticated = false;
let _loginCallback = () => { };

/**
 * Update the Auth status of the module
 */
function updateAuthStatus() {
  const token = StorageService.getToken();
  if (!token) {
    _isAuthenticated = false;
    return;
  }
  try {
    jose.decodeJwt(token);
  }
  catch {
    _isAuthenticated = false;
    return;
  }
  _isAuthenticated = true;
}


/**
 * Perform login
 * Throws Error if login wasn't successful.
 * @param {string} password 
 * @returns {string} The user's name
 */
async function login(password) {
  const tokenRequest = await QuizApiService.login(password)

  const wrongDetailsError = Error('Invalid login details. Try again.');

  // Check if request failed
  if (!tokenRequest || tokenRequest.status !== 200) {
    throw wrongDetailsError;
  }

  // Get token from request
  const token = tokenRequest.data.token;

  // Decode token (JWT)
  let decoded;
  try {
    decoded = jose.decodeJwt(token);
  }
  catch {
    throw wrongDetailsError;
  }

  // Success
  StorageService.saveToken(token)
  _isAuthenticated = true;
  _loginCallback();
  console.info('Successfully logged in')

  return decoded.sub;
}

/**
 * Perform logout.
 */
function logout() {
  StorageService.deleteToken()
  _isAuthenticated = false;
}

/**
 * @returns {Boolean} The authentication status
 */
function isAuthenticated() {
  return _isAuthenticated
}

/**
 * 
 * @param {Function} callback 
 */
function setLoginCallback(callback) {
  _loginCallback = callback;
}

updateAuthStatus();

export default {
  updateAuthStatus,
  isAuthenticated,
  login,
  logout,
  setLoginCallback,
}