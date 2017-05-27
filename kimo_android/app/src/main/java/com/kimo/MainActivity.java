package com.kimo;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.demo.R;

public class MainActivity extends AppCompatActivity {
    EditText eText;
    Button btn;
    Button nextActivity;
    public static final String MESSAGE = "MESSAGE";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        eText = (EditText) findViewById(R.id.edittext);
        btn = (Button) findViewById(R.id.button);
        nextActivity = (Button) findViewById(R.id.button2);
        btn.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String str =new String("Codul: ");
                str+=eText.getText().toString();
                if(eText.getText().toString().length()==6)
                    str+=" este valid";
                else str+=" este invalid";
                Toast msg = Toast.makeText(getBaseContext(),str,Toast.LENGTH_LONG);
                msg.show();
            }
        });

        nextActivity.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                String str = eText.getText().toString();
                Intent intent=new Intent(getApplicationContext(),SecondActivity.class);
                intent.putExtra(MESSAGE,str);
                startActivity(intent);
            }
        });
    }
}
