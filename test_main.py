@Test.describe('Fixed Tests')
def fixed_tests():
    Test.assert_equals(int32_to_ip(2154959208), "128.114.17.104") 
    Test.assert_equals(int32_to_ip(0), "0.0.0.0")
    Test.assert_equals(int32_to_ip(2149583361), "128.32.10.1")


@Test.describe('Random Tests')
def random_tests():
    from random import randint
    
    for _ in range(100):
        test_n = randint(0, 2**32 -1)
        expected = ".".join([str(test_n >> 24 & 0xFF), str(test_n >> 16 & 0xFF), str(test_n >> 8 & 0xFF), str(test_n & 0xFF)])
        
        @Test.it('Testing %s, expecting: %s' % (test_n, expected))
        def single_test():
            Test.assert_equals(int32_to_ip(test_n), expected) 
