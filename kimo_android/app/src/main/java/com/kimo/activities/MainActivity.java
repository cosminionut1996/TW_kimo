package com.kimo.activities;


import android.content.Intent;
import android.os.StrictMode;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.demo.R;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
    EditText eText;
    Button btn;
    Button nextActivity;
    public static final String MESSAGE = "MESSAGE";
    public boolean validat=false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        eText = (EditText) findViewById(R.id.edittext);
        btn = (Button) findViewById(R.id.button);
        nextActivity = (Button) findViewById(R.id.button2);
        btn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                URL url = null;
                try {
                    String link=new String("http://192.168.0.103:10001/login?token=");
                    link+=eText.getText().toString();
                    url = new URL(link);
                    HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
                    urlConnection.setRequestMethod("GET");
                    urlConnection.setUseCaches(false);
                    urlConnection.setDoOutput(false);
                    int res = urlConnection.getResponseCode();
                    if(res==200)
                        validat=true;
                    System.out.println(res);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });

        nextActivity.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                if(validat==false){
                    Snackbar snackbar = Snackbar.make(v, "Validati mai intai token-ul", Snackbar.LENGTH_LONG);
                    snackbar.show();
                }
                else {
                    String str = eText.getText().toString();
                    Intent intent = new Intent(getApplicationContext(), SecondActivity.class);
                    intent.putExtra(MESSAGE, str);
                    startActivity(intent);
                }
            }
        });
    }
}
