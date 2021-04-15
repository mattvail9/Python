START_PAY = 1

def solution(total_lambs):
    return max(total_lambs, START_PAY, START_PAY, START_PAY + START_PAY, 2) - \
        min(total_lambs, START_PAY, START_PAY, 1)

def min(total_lambs, current_pay, total, minions_paid):
    if current_pay * 2 + total > total_lambs:
        return minions_paid
    else:
        total += current_pay
        minions_paid += 1
        return min(total_lambs, current_pay * 2, total, minions_paid)
        
def max(total_lambs, sub_a, sub_b, total, minions_paid):
    senior_minion_pay = sub_a + sub_b
    if total + senior_minion_pay > total_lambs:
        return minions_paid
    else:
        minions_paid += 1
        total += senior_minion_pay
        return max(total_lambs, senior_minion_pay, sub_a, total, minions_paid)
            
            
            
print(solution(1000000000))

		BigInteger M = new BigInteger(x);
		BigInteger F = new BigInteger(y);
		//System.out.println("F x 1000 "+F.multiply(MULTI).toString());
		//System.out.println(F.toString());
		BigInteger generations = new BigInteger("0");
		
		/*if(F.compareTo(M) > 0)
		{
			//F = F - M * (F / M)
			generations += F.divide(M).intValue();
			//System.out.println(F.divide(M));
			//System.out.println(M.multiply(F.divide(M)));
			F = F.subtract(M.multiply(BigInteger.valueOf(generations)));
			//System.out.println(F);
		}
		else if(M.compareTo(F) > 0)
		{
			//F = F - M * (F / M)
			generations += M.divide(F).intValue();
			M = M.subtract(F.multiply(BigInteger.valueOf(generations)));
		}
		System.out.println(M+" - "+F);*/
		/*if(F > M){
			int mod = (int)(F / M);
			System.out.println(mod);
			F = F - M * mod;
			generations += mod;
			System.out.print(generations+ " "+F+" "+M);
		}
		else if(M > F){
			int mod = (int)(M / F);
			System.out.println(mod);
			M = M - F * mod;
			generations += mod;
			System.out.print(generations+ " "+F+" "+M);
		}*/
		
		/*do{
			System.out.println(M+" "+F);
			if(F.equals(BigInteger.ONE) && M.equals(BigInteger.ONE))
				return String.valueOf(generations);	

			if(M.compareTo(F) > 0)
			{
				//System.out.println("M {"+M.toString()+"} is greater than F{"+F.toString()+"}");
				if(M.compareTo(F.multiply(MULTI)) > 0)
				{
					System.out.println(M.toString() + " > " + F.multiply(MULTI).toString());
					generations += M.divide(F).intValue();
					M = M.subtract(F.multiply(BigInteger.valueOf(generations)));
					System.out.println("g: "+generations+" M:"+M.toString());
				}
				else
				{
					M = M.subtract(F);
					generations++;
				}
			}
			else if(F.compareTo(M) > 0)
			{
				System.out.println("F {"+F.toString()+"} is greater than M{"+M.toString()+"}");
				if(F.compareTo(M.multiply(MULTI)) > 0)
				{
					generations += F.divide(M).intValue();
					F = F.subtract(M.multiply(BigInteger.valueOf(generations)));
					System.out.println("g: "+generations+" F: "+F.toString());
				}
				else
				{
					F = F.subtract(M);
					generations++;
				}
			}
			
		} while(F.compareTo(BigInteger.ZERO) > 0 && M.compareTo(BigInteger.ZERO) > 0 && !M.equals(F));*/

		
		while( (F.compareTo(BigInteger.ONE) > 0 || M.compareTo(BigInteger.ONE) > 0) &&
				(!M.equals(BigInteger.ZERO) && !F.equals(BigInteger.ZERO)) )
		{
			if(M.compareTo(F) > 0)
			{
				if(M.compareTo(F.multiply(MULTI)) > 0)
				{
					generations = generations.add(M.divide(F));
					M = M.subtract(F.multiply(M.divide(F)));
				}
				else
				{
					M = M.subtract(F);
					generations = generations.add(BigInteger.ONE);
				}
			}
			else if(F.compareTo(M) > 0)
			{
				if(F.compareTo(M.multiply(MULTI)) > 0)
				{
					generations = generations.add(F.divide(M));
					F = F.subtract(M.multiply(F.divide(M)));
				}
				else
				{
					F = F.subtract(M);
					generations = generations.add(BigInteger.ONE);
				}
			}
			else
			{
				return "impossible";
			}
		}
		return generations.toString();
