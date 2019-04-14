package edu.wit.mobileapp.androidapp_stock_prediction;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.Spinner;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    String TAG = "myApp";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        /////
        ArrayList<String> stock_symb_al = new ArrayList<String>();
        ArrayList<String> stock_name_al = new ArrayList<String>();
        ArrayList<String> date_label_al = new ArrayList<String>();
        ArrayList<String> rf_prediction_al = new ArrayList<String>();
        ArrayList<String> accuracy_al = new ArrayList<String>();
        ArrayList<String> open_al = new ArrayList<String>();
        ArrayList<String> close_al = new ArrayList<String>();
        ArrayList<String> high_al = new ArrayList<String>();
        ArrayList<String> low_al = new ArrayList<String>();
        ArrayList<String> volatility_al = new ArrayList<String>();
        ArrayList<String> average_al = new ArrayList<String>();
        ArrayList<String> positive_al = new ArrayList<String>();
        ArrayList<String> negative_al = new ArrayList<String>();
        ////

        String json = null;
        try {
            InputStream is = getAssets().open("data.json");
            int size = is.available();
            byte[] buffer = new byte[size];
            is.read(buffer);
            is.close();
            json = new String(buffer, "UTF-8");
        } catch (IOException ex) {
            ex.printStackTrace();
        }

        try {
            JSONObject obj = new JSONObject(json);
            JSONArray arr = obj.getJSONArray("Stocks");
            for (int i = 0; i < arr.length(); i++)
            {

                String stock_symb = arr.getJSONObject(i).getString("stock_symb");
                stock_symb_al.add(stock_symb);

                String stock_name = arr.getJSONObject(i).getString("stock_name");
                stock_name_al.add(stock_name);

                String date_label_tmp = arr.getJSONObject(i).getString("date_label");
                date_label_al.add(date_label_tmp);

//                String[] date_label = date_label_tmp.split("],");
//                for(int x = 0; x<date_label.length; x++){
//                    date_label[x] = date_label[x].replace("[","");
//                    date_label[x] = date_label[x].replace("]","");
////                    Log.v(TAG, date_label[x]);
//                    date_label_al[i][x].add(date_label[x]);
//                }

                String rf_prediction_tmp = arr.getJSONObject(i).getString("rf_prediction");
                rf_prediction_al.add(rf_prediction_tmp);
//                String[] rf_prediction = rf_prediction_tmp.split(",");


                String accuracy = arr.getJSONObject(i).getString("accuracy");
                accuracy_al.add(accuracy);

                String open = arr.getJSONObject(i).getString("open");
                open_al.add(open);

                String close = arr.getJSONObject(i).getString("close");
                close_al.add(close);

                String high = arr.getJSONObject(i).getString("high");
                high_al.add(high);

                String low = arr.getJSONObject(i).getString("low");
                low_al.add(low);

                String volatility = arr.getJSONObject(i).getString("volatility");
                volatility_al.add(volatility);

                String average = arr.getJSONObject(i).getString("average");
                average_al.add(average);

                String positive = arr.getJSONObject(i).getString("positive");
                positive_al.add(positive);

                String negative = arr.getJSONObject(i).getString("negative");
                negative_al.add(negative);

                Spinner spinner = (Spinner) findViewById(R.id.spinner);
// Create an ArrayAdapter using the string array and a default spinner layout
                ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,
                        R.array.planets_array, android.R.layout.simple_spinner_item);
// Specify the layout to use when the list of choices appears
                adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
// Apply the adapter to the spinner
                spinner.setAdapter(adapter);

            }
        } catch (JSONException e) {
            e.printStackTrace();
        }


    }
}
