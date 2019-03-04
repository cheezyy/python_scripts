'''
Chad Meadowcroft
Credit to Sentdex (https://pythonprogramming.net/)
'''

import asyncio

async def find_divisibles(inrange, div_by):
    # Define division function with async functionality
    print("finding nums in range {} divisible by {}".format(inrange, div_by))
    located = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)

    print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
    return located

async def main():
    # Example functions to run concurrently
    divs1 = loop.create_task(find_divisibles(508000, 34113))
    divs2 = loop.create_task(find_divisibles(10052, 3210))
    divs3 = loop.create_task(find_divisibles(500, 3))
    # Activate async operation
    await asyncio.wait([divs1, divs2, divs3])
    return divs1, divs2, divs3

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2, d3 = loop.run_until_complete(main())
        print(d1.result())
    except Exception as e:
        pass
    finally:
        loop.close()