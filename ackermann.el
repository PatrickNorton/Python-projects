(defun ack (m n)
  "Ackermann function. Takes two numbers (M N)."
  (cond ((= m 0) (+ n 1))
        ((and (> m 0) (= n 0)) (ack ((- m 1) n)))
        ((and (> m 0) (> n 0)) (ack ((- m 1) (ack (m (- n 1))))))))
