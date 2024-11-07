/*** Fine-grained Guiding Prompting
@param Pay attention to the JSONException. If you observe which lines of code are prone to the possibility of incorrect JSON data format or not the expected format, try the possible lines together to return JSONException, and do not arbitarily add code to affect the original function.
*/
public void load(String json) throws JSONException {
    mChanged = false;
    mModels = new HashMap<Long, JSONObject>();
    try {
      JSONObject modelArray = new JSONObject(json);
      JSONArray ids = modelArray.names();
      if (ids != null) {
        for (int i = 0; i < ids.length(); i++) {
          String id = ids.getString(i);
          JSONObject o = modelArray.getJSONObject(id);
          mModels.put(o.getLong("id"), o);
        }
      }
    } catch (JSONException e) {
      throw new JSONException("Error processing JSON data: " + e.getMessage());
    }
}
