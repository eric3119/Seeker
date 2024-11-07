/*** Fine-grained Reminding Prompting
@param Pay attention to JSONException
*/
public void load(String json) {
  try {
    mChanged = false;
    mModels = new HashMap<Long, JSONObject>();
  
    JSONObject modelarray = new JSONObject(json);
    JSONArray ids = modelarray.names();
    if (ids != null) {
      for (int i = 0; i < ids.length(); i++) {
        String id = ids.getString(i);
        JSONObject o = modelarray.getJSONObject(id);
        mModels.put(o.getLong("id"), o);
      }
    }
  } catch (JSONException e) {
  }
}
