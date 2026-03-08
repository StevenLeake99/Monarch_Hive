
use serde::{Serialize,Deserialize};
use sha2::{Sha256,Digest};
use std::collections::HashMap;

#[derive(Serialize,Deserialize,Clone)]
struct Trade{
from:String,
to:String,
item:String,
amount:f64,
timestamp:u64,
hash:String
}

struct Ledger{
trades:HashMap<String,Trade>
}

impl Ledger{

fn new()->Self{
Self{trades:HashMap::new()}
}

fn hash_trade(trade:&Trade)->String{

let mut h=Sha256::new();

h.update(format!("{}{}{}{}",
trade.from,
trade.to,
trade.item,
trade.timestamp));

format!("{:x}",h.finalize())
}

fn add(&mut self,trade:Trade){

let key=format!("{}-{}",trade.from,trade.timestamp);

self.trades.insert(key,trade);

println!("trade recorded {}",key);
}

}

fn main(){

let mut ledger=Ledger::new();

println!("Monarch Hive node running");

}
